import com.alibaba.fastjson.JSONObject;
import fig.basic.Pair;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by chengiant on 16-11-15.
 */
public class processZhiDao {
    public static String StringFilter(String str) {
        // 只允许字母和数字 // String regEx ="[^a-zA-Z0-9]";
        // 清除掉所有特殊字符
        Pattern pattern = null;
        if (pattern == null) {
            //String regEx = "[`~!@#$%^&*()+=|{}':;',\\[\\]./?~！@#￥%……&*（）——+\\-－|{}【】‘；：”“’。，、？\\\\_～《》｛｝×＃￥％＆]";
            //String regEx="[`~!@#$%^&*()+=|{}':;',\\[\\].<>/?~！@#￥%……&*（）——+|{}【】‘；：”“’。，、？]";
            String regEx = "[`~!@#$%^&*()+=|{}':;',\\[\\]./?~！@#￥%……&*（）——+\\-－|{}<>【】‘；：”“’。，、？\\\\_～《》｛｝×＃￥％＆\"]";
            pattern = Pattern.compile(regEx);
        }
        String pre = ChineseUtil.cleanString(str);
        Matcher m = pattern.matcher(pre);
        String ss =  m.replaceAll("").trim();
        return ss;
    }
    static class Dealer_3 implements Runnable{
        private ConcurrentLinkedQueue<Pair<String,String>> in_queue;
        private ConcurrentLinkedQueue<Pair<String,String>> out_queue;
        NlpTool npt;
        Lexcon lexcon;
        List<Entity> ent_list;
        int max_q_length = 50;
        int max_a_length = 50;
        public Dealer_3(){}
        public Dealer_3(NlpTool npt, Lexcon lexcon,List<Entity> entityList, int max_q_length, int max_a_length,
                        ConcurrentLinkedQueue<Pair<String,String>> in,ConcurrentLinkedQueue<Pair<String,String>> out){
            this.in_queue = in;
            this.out_queue = out;
            this.npt = npt;
            this.lexcon = lexcon;
            this.ent_list = entityList;
            this.max_q_length = max_q_length;
            this.max_a_length = max_a_length;

        }
        private boolean isNumeric(String str){
            return str.matches("[-]?\\d+[.]?\\d+");
        }

        public void run() {
            while(true) {
                while (!in_queue.isEmpty()) {
                    String ret = "";
                    Pair<String,String> sentence = in_queue.poll();
                    if (sentence == null) {
                        continue;
                    }
                    String question = sentence.getFirst();
                    String answer = sentence.getSecond();
                    if (sentence == null) {
                        continue;
                    }
                    question = question.replaceAll("\\s+", "");
                    answer = answer.replaceAll("\\s+","");
                    question = StringFilter(question);
                    answer = StringFilter(answer);
                    if (question.length() <= 2) {
                        continue;
                    }
                    if (answer.length() <= 2) {
                        continue;
                    }
                    if (question.contains("http:") || question.contains("href")) {
                        continue;
                    }
                    if (answer.contains("http:") || answer.contains("href") ) {
                        continue;
                    }
                    /* question */
                    String q_seg = npt.ApplySimpleSeg(question);
                    String[] pp = q_seg.split(" ");
                    if (pp.length > max_q_length) {
                        continue;
                    }
                    String s = "";
                    boolean has_super_long = false;
                    for (int j=0; j < pp.length; j++) {
                        if (pp[j].length() > 10) {
                            has_super_long = true;
                            break;
                        }
                        if (isNumeric(pp[j])) {
                            s = s + "<NUMBER>";
                        }else {
                            s = s + pp[j];
                        }
                        if (j < pp.length -1) {
                            s = s + " ";
                        }

                    }
                    if (has_super_long) {
                        continue;
                    }
                    q_seg = s;

                    Pair<String,List<Pair<Entity,String>>> nered = lexcon.doLexcon(q_seg, ent_list, new HashMap<>());
                    String q_lex = nered.getFirst();

                    /* answer */
                    String a_seg = npt.ApplySimpleSeg(answer);
                    pp = a_seg.split(" ");
                    if (pp.length > max_a_length) {
                        continue;
                    }
                    s = "";
                    has_super_long = false;
                    for (int j=0; j < pp.length; j++) {
                        if (pp[j].length() > 10) {
                            has_super_long = true;
                            break;
                        }
                        if (isNumeric(pp[j])) {
                            s = s + "<NUMBER>";
                        }else {
                            s = s + pp[j];
                        }
                        if (j < pp.length -1) {
                            s = s + " ";
                        }

                    }
                    if (has_super_long) {
                        continue;
                    }
                    a_seg = s;

                    nered = lexcon.doLexcon(a_seg, ent_list, new HashMap<>());
                    String a_lex = nered.getFirst();

                    out_queue.add(new Pair<>(q_lex, a_lex));
                }
                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    static class Writer_3 implements Runnable{
        private PrintWriter pw;
        private ConcurrentLinkedQueue<Pair<String,String>> queue;
        public Writer_3(){}
        int counter = 0;
        public Writer_3(PrintWriter pw,ConcurrentLinkedQueue<Pair<String,String>> queue){
            this.pw = pw;
            this.queue = queue;
        }
        public void run() {
            while(true){//循环监听
                while(!queue.isEmpty()){
                    counter = counter +1;
                    Pair<String,String> pp = queue.poll();
                    if (pp == null) {
                        continue;
                    }
                    pw.println(pp.getFirst() + "###===>###" + pp.getSecond());
                    if (Math.floorMod(counter, 1000) == 0) {
                        pw.flush();
                    }
                }
                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    public static void main(String[] args) throws Exception {
        String dest_file = "./zhidao-train.txt";

        String src_file = "./zhidao.bson";
        String lexconEntities = "";
        int thread_num = 1;
        int max_question_length = 50;
        int max_answer_length = 50;
        int maxQ = 1000;
        for (int i = 0; i < args.length; i += 1) {
            String arg = args[i];
            if (arg.startsWith("--")) {
                arg = arg.substring(2);
            } else if (arg.startsWith("-")) {
                arg = arg.substring(1);
            }
            if (arg.equalsIgnoreCase("src")) {
                src_file = args[i + 1];
            } else if (arg.equalsIgnoreCase("dest")) {
                dest_file = args[i + 1];
            } else if (arg.equalsIgnoreCase("lexcon")) {
                lexconEntities = args[i + 1];
            } else if (arg.equalsIgnoreCase("thread")) {
                thread_num = Integer.valueOf(args[i + 1]);
            }else if (arg.equalsIgnoreCase("max_question_length")) {
                max_question_length = Integer.valueOf(args[i + 1]);
            }else if (arg.equalsIgnoreCase("max_answer_length")) {
                max_answer_length = Integer.valueOf(args[i + 1]);
            }
        }
        List<Entity> entity_list = new ArrayList<>();
        String[] arr = lexconEntities.split(",");
        for (int j =0; j < arr.length; j++) {
            Entity ent = Entity.valueOf(arr[j]);
            if (ent != null) {
                entity_list.add(ent);
            }
        }
        PrintWriter pw = new PrintWriter(new OutputStreamWriter(new FileOutputStream(dest_file), "UTF-8"), true);

        File file_src = new File(src_file);
        int count = 0;
        NlpTool npt = new NlpTool();
        Lexcon lexcon = Lexcon.getSingleton();

        ConcurrentLinkedQueue<Pair<String,String>> in_queue = new ConcurrentLinkedQueue<>();
        ConcurrentLinkedQueue<Pair<String,String>> out_queue = new ConcurrentLinkedQueue<>();
        for(int j=0;j<thread_num;j++){
            Thread t = new Thread(new Dealer_3(npt,lexcon,entity_list,max_question_length,max_answer_length, in_queue,out_queue));
            t.setDaemon(true);
            t.start();//多线程往队列中写入数据

        }
        Thread t = new Thread(new Writer_3(pw,out_queue));
        t.setDaemon(true);
        t.start();
        if (file_src.isFile() && file_src.exists()) {

            String encoding = "UTF8";
            InputStreamReader read = new InputStreamReader(new FileInputStream(file_src), encoding);
            BufferedReader bufferedReader = new BufferedReader(read);
            String lineTxt = null;
            while ((lineTxt = bufferedReader.readLine()) != null) {
                if (Math.floorMod(count, 100) == 0) {
                    System.out.printf("%c ============>  processed  sentences: %d ================", 13, count);
                }
                count++;
                JSONObject jsonObject = JSONObject.parseObject(lineTxt);
                String question = jsonObject.getString("question");
                String answer = jsonObject.getString("answer");

                while (true) {
                    if (in_queue.size() < maxQ) {
                        in_queue.add(new Pair<>(question, answer));
                        count ++;
                        break;
                    } else {
                        Thread.sleep(10);
                    }
                }
            }

        }
        while(!in_queue.isEmpty() || !out_queue.isEmpty()) {
            Thread.sleep(10);
        }
        pw.flush();
        System.out.println("\nDone!! total sentence = " + count);

    }
}

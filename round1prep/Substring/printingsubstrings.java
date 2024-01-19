import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your name:");
        
        String name = sc.nextLine();
        System.out.println("your name is"+name);
        System.out.println("length of my name is:"+name.length());
        int len = name.length();
        for(int i=0; i<len; i++){
           for(int j=i; j<len;j++){
               System.out.println(name.substring(i,j+1));
            }
        }
        
        
        
    }
}



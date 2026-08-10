package lab2;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class lab2 {
    private static Scanner sc = null;
    public static int[] constructArray() {
        System.out.println("Enter the number of elements");
        int  size = sc.nextInt();
        int[] arr = new int[size];
        for(int i=0;i< size;i++){
            arr[i] = sc.nextInt();
        }
        return arr;
    }
    public static void duplicate(int[] args) {

        for (int i = 0; i < args.length; i++) {
            for (int j = i + 1; j < args.length; j++) {
                if (args[i] == args[j]) {
                    System.out.println(args[i]);
                    break;
                }
            }
        }
    }
    public static void kth(int[] args) {
        System.out.println("Enter the k value");
        int k=sc.nextInt();
        Arrays.sort(args);
        if(k<0 || k> args.length){
            System.out.println("Invalid K");
        }
        int kthSmallest = args[k - 1];
        int kthLargest = args[args.length - k];
        System.out.println("Kth Smallest"+kthSmallest);
        System.out.println("Kth Largest"+kthLargest);

    }
    public static void qA() {
        System.out.println("Which country has the currency 'yang'");
        String a= "China";
        for(int i=0;i<3;i++){
            String b = sc.next();
            if(b.equals(a)){
                System.out.println("Good");
                break;
            }
        }
        System.out.println("Correct answer is"+a);

    }
    public static void pos(int[] arr) {
        int left = 0;
        int right = arr.length - 1;
        while (left <= right) {

            if (arr[left] < 0) {
                left++;
            }

            else if (arr[right] >= 0) {
                right--;
            }

            else {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
                right--;
            }
        }
        for (int j : arr) {
            System.out.println(j);
        }
    }

    public static void floyds() {
        System.out.println("Enter the number of rows");
        int row = sc.nextInt();


    }
    public static void mainApp() {
        int choice=0;
        do{
            System.out.println("********************Main App************************");
            System.out.println("1. Q1 Duplicate");
            System.out.println("2. Q2 Kth item ");
            System.out.println("3. Q3 Pos/Neg");
            System.out.println("4. Q4 Q/A");
            System.out.println("5. Q5");
            System.out.println("6. Exit");
            System.out.println("Enter your choice");
            choice = sc.nextInt();

            switch(choice){
                case 1:{
                    int[] arr =constructArray();
                    duplicate(arr);
                    break;
                }
                case 2:{
                    int[] arr =constructArray();
                    kth(arr);
                    break;
                }
                case 3:{
                    int[] arr =constructArray();
                    pos(arr);
                    break;

                }
                case 4:{
                    qA();
                }
                case 5:{

                }

            }
        }while (choice>0);

    }
    public static void main(String[] args) {
//        int[] i;
//        i = new int[5];
        String[] user = {"admin","user"};
        String[] password = {"abc","xyz"};
        sc = new Scanner(System.in);
        System.out.println("Enter username & password");
        String username =sc.next();
        String pass = sc.next();
        boolean checked = false;
        for(int i=0;i<user.length;i++){
            if((user[i].equals(username)) && (password[i].equals(pass))){
                checked = true;
                break;
            }
        }
        if(checked){
            mainApp();
        }
        else{
            System.out.println("Unauthorized user");
        }



    }
}

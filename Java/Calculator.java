package Java;

public class Calculator {
    public static class Calc {
        public Calc() {
        }
        private int add(int num1, int num2) {
            int ret = 0;
            ret = num1+num2;
            return ret;
        }
        
        private int multiply(int num1, int num2) {
            int ret = 0;
            ret = num1*num2;
            return ret;
        }

        private int subtract(int num1, int num2) {
            int ret = 0;
            ret = num1-num2;
            return ret;
        }
        
        private int divide(int num1, int num2) {
            int ret = 0;
            ret = num1/num2;
            return ret;
        }

        public void menu(int num1, int num2) {
            System.out.println("\n## -- MENU -- ##");
            System.out.println("1- Add\n2- Multiply\n3- Subtract\n4- Divide\n5- Exit\n");
            System.out.println("\n## --------- ##");

            java.util.Scanner scan = new java.util.Scanner(System.in);
            int choice = scan.nextInt();
            switch (choice) {
                case 1:
                    int retSum = this.add(num1, num2);
                    System.out.println("\n"+ retSum + "\n");
                    break;
                case 2:
                    int retMult = this.multiply(num1, num2);
                    System.out.println("\n"+ retMult + "\n");
                    break;
                
                case 3:
                    int retSub = this.subtract(num1, num2);
                    System.out.println("\n"+ retSub + "\n");
                    break;

                case 4:
                    int retDiv = this.divide(num1, num2);
                    System.out.println("\n"+ retDiv + "\n");
                    break;

                case 5:
                    System.out.println("\nSaindo do sistema....\n");
                    System.exit(0);
                    break;
                
                default:
                    System.out.println("\nEssa opção não é valida\n");
                    break;
            }

            scan.close();
        }
    }

    public static void main(String[] args) {
        Calc calcc = new Calc();

        while(true) {
            java.util.Scanner scan = new java.util.Scanner(System.in);
            int num1 = scan.nextInt();
            int num2 = scan.nextInt();
            calcc.menu(num1, num2);
            scan.close();
        }
    }
}

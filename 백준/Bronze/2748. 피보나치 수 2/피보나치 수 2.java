import java.util.Scanner;

public class Main {
    public static long fibo(int n) {
        if (n == 0 ) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }

        long prev1 = 0, prev2 = 1, result = 0;
        for (int i = 2; i <= n; i++) {
            result = prev1 + prev2;
            prev1 = prev2;
            prev2 = result;
        }
        return result;

    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int answer = scanner.nextInt();
        System.out.println(fibo(answer));
    }
}
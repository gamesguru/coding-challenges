package fastprepjava;

import java.util.PriorityQueue;

public class MicrosoftFindMaxSumWithSameFirstAndLastDigit {

    public static int findMaxSumWithSameFirstAndLastDigit(int[] nums) {

        // Process into 10 heaps, based on first digit
        PriorityQueue<Integer>[] pqs = new PriorityQueue[10];
        for (int i = 0; i < 10; i++) {
            pqs[i] = new PriorityQueue<>();
        }

        for (int num : nums) {
            String numStr = String.valueOf(num);
            int firstDigit = Integer.parseInt(String.valueOf(numStr.charAt(0)));
            pqs[firstDigit].add(num);
        }

        // Find max sum
        int maxSum = 0;
        for (int i = 0; i < nums.length; i++) {
            int sum = nums[i] + nums[nums.length - 1];
            if (sum > maxSum) {
                maxSum = sum;
            }
        }
        return maxSum;
    }

    public static void main(String[] args) {
        int[] nums = {2, 36, 45, 306, 415};
        int expected = 460;

        int actual = findMaxSumWithSameFirstAndLastDigit(nums);
        System.out.println("Expected: " + expected + ", Actual: " + actual);
        assert expected == actual;
    }
}

// Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

public class BuySellStock {

    // Two pointers solution:
    public int maxProfit1(int[] prices) {

        int left = 0, right = 1, maxProfit = 0;

        while (right < prices.length) {
            int currentProfit = prices[right]-prices[left];
            if (currentProfit > 0 && currentProfit > maxProfit) {
                maxProfit = currentProfit;
            } else {
                left = right;
            }
            right++;
        }

        return maxProfit;
    }
}

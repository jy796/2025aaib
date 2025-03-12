class Solution {
public:
    long long coloredCells(int n) {
        long long ans = n;// 很長很長的整數

        return ans*ans +(ans-1)*(ans-1);
    }
};

class Solution {
public:
    long long coloredCells(int n) {
        long long ans = n;// �ܪ��ܪ������

        return ans*ans +(ans-1)*(ans-1);
    }
};

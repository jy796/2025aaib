//week04-2.c �O���Ѫ� Leetcode �D�� Easy �O(�G�X�@)
//Leetcode 2529. Maxium Count of Postive Integer and Negative Integer
int maximumCount(int* nums, int numsSize) {
    int pos = 0, neg = 0;// �j��e��,�ǳƦn,����0

    for(int i=0; i<numsSize; i++) {
        if( nums[i] > 0 ) pos++; // ����
        if( nums[i] < 0 ) neg++; // �t��
    }//�j�餤���A��s�B�ק復
    //�j��᭱�A�⥦���ӥ�
    if(pos>neg) return pos; //���Ƥ���h,����
    else return neg; // ���M,�N�t��
    }

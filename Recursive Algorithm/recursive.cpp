#include<iostream>
#include<algorithm>
using namespace std;

//========================Fibonacci数列========================
//递归写法
int F(int n) {
    if (n==0 || n==1)
        return 1;
    else
        return F(n-1) + F(n-2);
}

//改进：递归写法包含重复计算如F(4)=F(3)+F(2),而F(3)=F(2)+F(1),F(2)重复计算了
//古可开辟一维数组保存
const int maxV = 100;

int F(int n, int *dp) {
    if (n==0 || n==1)
        return 1;//递归边界
    if (dp[n] != -1) {
        return dp[n];
    } else {
        dp[n] = F(n-1, dp) + F(n-2, dp);
        return dp[n];
    }
}

// int main() {
//     int dp[maxV];
//     fill(dp, dp+maxV, -1);
//     cout<<F(5)<<endl;
//     cout<<F(5, dp)<<endl;
//     return 0;
// }



//========================全排列========================
const int maxn = 11;
int n, P[maxn], hashTable[maxn] = {false};//P为当前排列，hashTable记录整数x是否已在P中
void generateP(int index) {//填第index位
    if (index == n+1) {//递归边界
        for (int i = 1; i <= n; i++) {
            cout<<P[i];//输出当前排列
        }
        cout<<endl;
        return;
    }
    for (int x = 1; x <= n; x++) {//枚举1-n位，试图将x填入p[index]
        if (hashTable[x] == false) {//若x未使用
            P[index] = x;//将x填入index位
            hashTable[x] = true;//标记x为已使用
            generateP(index+1);//处理第index+1
            hashTable[x] = false;//还原，即该index位上不使用x
        }
    }
}
// int main() {
//     n = 3;
//     generateP(1);
//     return 0;
// }



//========================N皇后问题========================
//两两均不在同一行同一列同一对角线上
//P的位数确保不再同一行，P每一位上的数字不同保证不再同一列，
//此时就是一个全排列，只要保证不再同一对角线即可
int cnt;
void generatePforQ(int index) {
    if (index == n+1) {
        bool flag = true;
        //判段全排列是否在同一对角线
        for (int i = 1; i <= n; i++) {
            for (int j = i+1; j <= n; j++) {
                if (abs(i-j) == abs(P[i]-P[j]))
                    flag = false;
            }
        }
        if (flag) {
            cnt++;
        }
        return;
    }
    for (int x = 1; x <= n; x++) {
        if (hashTable[x] == false) {
            P[index] = x;
            hashTable[x] = true;
            generatePforQ(index+1);
            hashTable[x] = false;
        }
    }
}

// 改进：递归到某一层由于一些事实不需要往下一个子问题递归
// 就可以直接返回上一层，叫做回溯法
void generatePforQBetter(int index) {
    if (index == n + 1) {
        cnt++;
        return;
    }
    for (int x = 1; x <= n; x++) {
        if (!hashTable[x]) {
            bool flag = true;
            for (int pre = 1; pre < index; pre++) {
                if (abs(index-pre) == abs(x-P[pre])) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                P[index] = x;
                hashTable[x] = true;
                generatePforQBetter(index+1);
                hashTable[x] = false;
            }
        }
    }
}

int main() {
    n = 8;
    cnt = 0;
    // generatePforQ(1);
    generatePforQBetter(1);
    cout<<cnt<<endl;
    return 0;
}
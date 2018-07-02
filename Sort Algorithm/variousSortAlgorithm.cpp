#include<iostream>
#include<cstring>
#include<algorithm>

using namespace std;

// *******************sort algorithm*****************
//====================插入排序========================
// 直接插入排序
/**
将一个记录插入到之前已排好序的有序表中，默认将第一个元素看作有序表，依次插入后边的所有元素。
时间复杂度：O(n^2)
空间复杂度：O(1)
稳定，适合小数组
**/
void StrInsertSort(int *p, int n) {
    for (int i = 1; i < n; i++) {
        int tmp = p[i], j;
        for (j = i - 1; j >= 0 && tmp < p[j]; j--) {
            p[j+1] = p[j];
        }
        p[j+1] = tmp;
    }
}

// 折半插入排序
/**
基于直接插入改写，减少“移动”和“比较”次数。
时间复杂度：O(n^2)
空间复杂度：O(1)
稳定
**/
void  BInsertSort(int *p, int n) {
    for (int i = 0; i < n; i++) {
        int tmp = p[i], j;
        int low = 0, high = i-1;
        while (low <= high) {
            int m = (low + high) / 2;
            if (tmp < p[m]) {
                high = m - 1;
            } else {
                low = m + 1;
            }
        }
        for (j = i-1; j >= high+1; j--) {
            p[j+1] = p[j];
        }
        p[j+1] = tmp;

    }
}

// 希尔排序
/**
直接对插入排序进行改进，又称“缩小增量排序”
时间复杂度：O(n^2)
空间复杂度：O(1)
不稳定
**/
void ShellInsertSort(int *p, int n) {
    int step = n / 2;
    while (step >= 1) {
        for (int i = step; i < n; i ++) {
            int tmp = p[i], j;
            for (j = i - step; j >= 0 && tmp < p[j]; j -= step) {
                p[j+step] = p[j];
            }
            p[j+step] = tmp;
        }
        step /= 2;
    }
}
// ===================交换排序========================
//冒泡排序
/**
两两比较相邻元素，第一次冒上来的是最小的元素，第二次是次小。
时间复杂度：O(n^2)
空间复杂度：O(1)
稳定
**/
void BubbleSort(int *p, int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = n-1; j > i; j--) {
            if (p[j] < p[j-1]) {
                int tmp = p[j];
                p[j] = p[j-1];
                p[j-1] = tmp;
            }
        }
    }
}

//快速排序
/**
通过一趟排序将元素分割成两个部分，左半部分比关键元素小，右半部分比关键元素大。即能确定关键元素最终所在位置。
时间复杂度：O(nlogn),最坏情况O(n^2)
空间复杂度：O(1)
不稳定
**/
void QuickSort(int *p, int l, int r) {
    if (l < r) {
        int i = l, j = r, x = p[i];
        while (i < j) {
            while (i < j && p[j] >= x)
                j--;
            if (i < j)
                p[i++] = p[j];
            while (i < j && p[i] <= x)
                i++;
            if (i < j)
                p[j--] = p[i];
        }
        p[i] = x;
        QuickSort(p, l, i-1);
        QuickSort(p, i+1, r);
    }
}
// ===================选择排序========================
//简单选择排序
/**
每一趟排序都会选出最小的(或最大的)值。
时间复杂度：O(n^2)
空间复杂度：O(1)
不稳定
**/
void SimSelectSort(int *p, int n) {
    for (int i = 0; i < n-1; i++) {
        int m = i;
        for (int j = i+1; j < n; j++) {
            if (p[j] < p[m])
                m = j;
        }
        int tmp = p[i];
        p[i] = p[m];
        p[m] = tmp;
    }
}

//堆排序
/**
利用堆这种数据结构的性质所设计的。
时间复杂度：O(nlogn)
空间复杂度：O(1)
**/
void HeapAdjust(int *p, int k, int n) {
    //第k个位置往下调整
    int tmp = p[k];//先取出当前元素
    for (int i = k*2+1; i < n; i = i*2 + 1) {//从ik结点的左子结点开始
        if (i + 1 < n && p[i] < p[i+1]) {
            //如果右子结点存在并且左子结点小于右子结点，i指向右子结点
            i++;
        }
        if (p[i] > tmp) {
            p[k] = p[i];//如果子结点大于父结点，将子结点值赋给父结点,不用交换
            k = i;//并且父结点位置更新
        } else {
            break;
        }
    }
    p[k] = tmp; //将tmp放到最终位置
}
void HeapSort(int *p, int n) {
    //将p构造一个大顶堆
    //从0到n/2-1都有孩子节点
    for (int i = n/2-1; i >= 0; i--) {
        HeapAdjust(p, i, n);
    }
    //调整堆结构+交换堆顶元素与末尾元素
    for (int j = n-1; j > 0; j--) {
        swap(p[j], p[0]);
        HeapAdjust(p, 0, j);//重新对堆进行调整
    }
}

// ===================归并排序========================
/**
将两个或两个以上的有序表组合成一个有序表，采用分治法实现
时间复杂度:O(nlogn)
空间复杂度：O(n)
稳定
**/
void Merge(int *p, int l, int m, int r) {
    int i = l, j = m+1, t = 0;
    int tmp[r-l+1];
    while (i <= m && j <= r) {
        if (p[i] <= p[j]) {
            tmp[t++] = p[i++];
        } else {
            tmp[t++] = p[j++];
        }
    }
    while (i <= m)
        tmp[t++] = p[i++];
    while (j <= r) 
        tmp[t++] = p[j++];
    t = 0;
    while (l <= r) {
        p[l++] = tmp[t++];
    }
}
void MergeSort(int *p, int l, int r) {
    if (l < r) {
        int m = (l + r) / 2;
        MergeSort(p, l, m);
        MergeSort(p, m+1, r);
        Merge(p, l, m, r);
    }
}

//====================基数排序========================
//基数排序
/**
依次按每个基数位上的数字排序，数字基数为10,字母基数为26。
每个基数位上数字排序分为：分配，收集两个过程
时间复杂度：O(d(n+r))
空间复杂度：O(n+r)
稳定
**/
//取数据i,d位上的数字
int getDigit(int i, int d) {
    int tmp;
    while (d--) {
        tmp = i % 10;
        i /= 10;
    }
    return tmp;
}
/**
n:数据个数
radix:基数个数，数字为1-9总共10个基数，字母为a-z总共26个基数
dis:数据中最多基数个数，即最多位数。
**/
int RadixSort(int *p, int n, int radix, int dis) {
    int i = 0, v;
    int count[radix];//每个基数存放数据个数
    int bucket[n];//暂存数据
    for (int d = 1; d <= dis; d++) {
        //置空每个桶(基数)
        fill(count, count+radix, 0);
        //统计每个桶所存放数据个数
        for (i = 0; i < n; i++) {
            v = getDigit(p[i],d);
            count[v]++;
        }
        //计算每个桶的右边界索引
        for (i = 1; i < radix; i++) {
            count[i] += count[i-1];//count[i]表示第i个桶的右边界索引
        }
        //分配数据,从后往前取，因为知道的是每个桶的索引右边界，通过--来存放，为了保证稳定
        for (i = n-1; i >= 0; i--) {
            v = getDigit(p[i], d);
            bucket[--count[v]] = p[i];
        }
        //收集数据
        memcpy(p, bucket,sizeof(bucket));
    }
}

void print(int *p, int n) {
    for (int i = 0; i < n; i++) {
        if (i <  n - 1) {
            cout<<p[i]<<',';
        } else {
            cout<<p[i]<<'.'<<endl;
        }
    }
}

int main() {
    int arr[5] = {2,5,3,1,4};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout<<"排序前：";
    print(arr, n);

    RadixSort(arr, n, 10, 1);
    cout<<"排序后：";
    print(arr,n);
    return 0;
}

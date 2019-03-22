#include<iostream>
#include <math.h> 
// Problem : https://practice.geeksforgeeks.org/problems/power-of-2/0?fbclid=IwAR3NN1eZZlzYBKBR-EyREwyRc_MgU67C9GgX_LIqghZtozdgU4QEDFdQcSA
using namespace std;
int main()
 {
     int T;
     long int N;
     cin>>T;
     for (int i =0;i<T;i++)
     {
        cin>>N;
        if(!(log2(N)-int(log2(N)))){
            cout<<"YES"<<endl;
        }
        else {
            cout<<"NO"<<endl;
        }
     }
	return 0;
}
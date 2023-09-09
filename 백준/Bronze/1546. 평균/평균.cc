#include <iostream>
using std::cin;
using std::cout;


int main(){
    int N;
    cin >> N;
    double score[1001];
    for(int i = 0; i < N;i++){
        cin>>score[i];
    }
    double Max = 0;
    
    for(int i = 0; i < N;i++){
        if(Max < score[i]){
            Max = score[i];
        }
    }
    
    for(int i = 0; i < N;i++){
        score[i] = score[i]/Max*100;
    }

    double A = 0;

    for(int i = 0; i < N;i++){
        A += score[i];
    }
    
    cout << A/N;
}
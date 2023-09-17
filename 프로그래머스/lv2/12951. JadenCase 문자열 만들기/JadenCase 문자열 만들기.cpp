#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    int flag = 0;
    for(int i = 0; i<s.length();i++){
        if(i==0){
            if('a'<= s[i] && s[i] <='z'){
                answer += (s[i] - 32);
            }
            else if(s[i]==' '){
                answer+=s[i];
                flag++;
            }
            else{
                answer+=s[i];
            }
        }
        else if(flag == 0 && 'A'<= s[i] && s[i]<='Z'){
            answer += (s[i] + 32);
        }
        else if(s[i] == ' '){
            answer += ' ';
            flag = 1;
        }
        else if(flag == 1 && 'a'<= s[i] && s[i] <='z'){
            answer+=(s[i]- 32);
            flag = 0;
        }
        else if(flag == 1 && 'a'>= s[i] && s[i]<='z'){
            answer+= s[i];
            flag = 0;
        }
        
        else{
            answer += s[i];
        }
    }
    return answer;
}
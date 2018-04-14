/* 	Program to Find the Largest & Smallest Word in a String
	made by 	: rakesh kumar
*/
#include <iostream>
#include <string.h>
#include <ctype.h>
using namespace std;
int main()
	{
       char string[100], word[20], max[20], min[20], c;
       int i = 0, j = 0, flag = 0;
       cout<<"Enter string: ";
       cin.getline(string,100);
	   	
		//processing phase
		for (i = 0; i < strlen(string); i++)
        {
           while (i < strlen(string) && !isspace(string[i]) && isalnum(string[i]))
            {
              word[j++] = string[i++];
            }
            if (j != 0)
            {
              word[j] = '\0';
              
			  if (flag==0)       // this will run only once 
               {
                flag = 1;
                strcpy(max, word);
                strcpy(min, word);
               }
              if (strlen(word) > strlen(max))
                {
                  strcpy(max, word);
                }
                if (strlen(word) < strlen(min))
                {
                    strcpy(min, word);
                }
              j = 0;   // for next word in the string
            }
        }

	//output phase
    cout<<"The largest word is '"<<max <<"' and smallest word is '"<<min<<"' in ''"<<string<<"'";
    return 0;
}

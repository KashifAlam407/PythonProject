#include <stdio.h>

void guess();

int main()
{
    printf("Guess a Number between 1 and 100: \n");
    guess();
    return 0;
}

int num;

void guess(){
    int r = 44;
    int i = 1;
    while (i<100){
        scanf("%d", &num);

        if (num>r){
            printf("Guess a number less than: %d \n", num);
            
        }
        else if (num<r){
            printf("Guess a number bigger than: %d \n", num);
        }
        else{
            printf("Congratulation! You have guessed the right number. \n");
            break;
        }
        i++;
    }
    int score = 100/i;
    printf("---------------------------------------\n");
    printf("-----------");
    printf("Your score is: %d", score);
    printf("-----------\n");
    printf("---------------------------------------");

    return;
    
}


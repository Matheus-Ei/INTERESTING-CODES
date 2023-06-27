#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>

char *listPointer;

void addNewElement()
{
    char list = {'M'};
    char listElement;
    listPointer = &list;
    
    printf("Lista atual: %s\n", list);
    printf("Diga qual elemento você deseja adicionar na lista: ");
    scanf("%s", &listElement);
    list = list + listElement;
    
}

int main()
{
    int response;
    
    while (true){
        printf("Diga se você deseja:\n");
        printf("1 - Adicionar um novo elemento na lista\n");
        printf("2 - Deletar um elemento da lista\n");
        printf("3 - Marcar um elemento da lista como concluido\n");
        scanf("%d", &response);
        
        if(response == 1){
            addNewElement();
        }
        else if (response == 2){
            
        }
        else if (response == 3){
            
        }
        else{
            printf("Você deve dizer um valor de 1 a 3, outros valores serão considerados invalidos\n");
        }
    }
    return 0;
}

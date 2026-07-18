#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
} Node;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}

int main() {
    Node* first = createNode(100);
    Node* second = createNode(200);

    // Link nodes
    first->next = second;
    second->prev = first;

    // Forward
    printf("Forward: ");
    Node* temp = first;
    while (temp != NULL) {
        printf("[%d] -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");

    // Backward
    printf("Backward: ");
    temp = second;
    while (temp != NULL) {
        printf("[%d] -> ", temp->data);
        temp = temp->prev;
    }
    printf("NULL\n");

    free(first);
    free(second);
    printf("Hello, World!\n");
    return 0;
}
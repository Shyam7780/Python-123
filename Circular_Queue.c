#include <stdio.h>
#define SIZE 5

int cqueue[SIZE];
int front = -1, rear = -1;

void enqueue(int value) {
    if ((front == 0 && rear == SIZE - 1) || (rear + 1) % SIZE == front) {
        printf("Circular Queue Overflow\n");
    } else {
        if (front == -1) front = 0;
        rear = (rear + 1) % SIZE;
        cqueue[rear] = value;
        printf("%d enqueued\n", value);
    }
}

void dequeue() {
    if (front == -1) {
        printf("Circular Queue Underflow\n");
    } else {
        printf("%d dequeued\n", cqueue[front]);
        if (front == rear) {
            front = rear = -1; // Queue becomes empty
        } else {
            front = (front + 1) % SIZE;
        }
    }
}

void display() {
    if (front == -1) {
        printf("Circular Queue is empty\n");
    } else {
        printf("Circular Queue elements: ");
        int i = front;
        while (1) {
            printf("%d ", cqueue[i]);
            if (i == rear) break;
            i = (i + 1) % SIZE;
        }
        printf("\n");
    }
}

int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);
    enqueue(40);
    display();
    dequeue();
    display();
    enqueue(50);
    enqueue(60); // This will wrap around
    display();
    return 0;
}

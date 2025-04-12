#ifndef QUEUE_H
#define QUEUE_H

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x;
    int y;
} Position;

typedef struct {
    Position *positions;
    int head;
    int tail;
    int size;
    int capacity;
} Queue;

#define QUEUE_SIZE 10

Queue* init();
int isEmpty(Queue *q);
int isFull(Queue *q);
void push(Queue *q, Position p);
Position pop(Queue *q);
void freeQueue(Queue *q);

#endif
#include <stdio.h>

typedef struct ExampleBook {
    int     sellingBookshops;
    int     isBestselling;
    double  salesMillions;
    float   sellingPrice;
} Book;

typedef struct ExampleBookshop {
    int     uniqueBooks;
    int     isOpen;
    float   totalValue;
} Bookshop;

int main() {
    Book book1 = {
    1, // sellingBookshops 
    1, // isBestselling
    65.73, // salesMillions
    7.99 // sellingPrice
    };

    Book book2 = {
    1, // sellingBookshops 
    0, // isBestselling
    0.934, // salesMillions
    9.99, // sellingPrice
    };

    printf("%d\n%d\n%lf\n%f\n", book1.sellingBookshops, book1.isBestselling, book1.salesMillions, book1.sellingPrice);
    printf("%d\n%d\n%lf\n%f\n", book2.sellingBookshops, book2.isBestselling, book2.salesMillions, book2.sellingPrice);
}
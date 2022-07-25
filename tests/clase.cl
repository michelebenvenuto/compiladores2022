class Main {
    a : Int <- 1;
    b : Int <- 2;
    c : Int <- 3; 

    main() : SELF_TYPE {
        {
            a <- a + b *c;
            self;
        }
    } ;

};
class Main {
    a : Int <- 1;
    b : Int <- 2;
    c : Int;

    main() : SELF_TYPE {
        {
            c <- a + d ;
            c <- a - d ;
            c <- a * d ;
            c <- a / d ;
            self;
        }
    } ;

};
class Main {
    a : Int <- 1;
    b : Int <- 2;
    c : Int;
    d : Int;

    main() : SELF_TYPE {
        {
            a <= b;
            self;
        }
    } ;

};
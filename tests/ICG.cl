class Main {
    a: Int;
    itr: Int;
    b: Int;

    sum(a: Int, b: Int): Int {
        a + b
    };

    main() : Int {
        {
            a <- sum(10 , b);
            while itr < 20 loop 
                if a < 10 then 
                    a <- 5+2 * 3
                else 
                    a <- 5*5 + 7
                fi 
            POOL;
            itr <-0;
        }
    };
};
class Results {

    ress: Int; 

    get_ress() : Int {
        ress
    };

    set_res(i: Int) : SELF_TYPE {
        {
            ress <- i;
            self;
        }
    };
};


class Factorial {
    factorial(n: Int) : Int {
      	 if n=0 then 0 else
         if n=1 then 1 else
        	n*factorial(n-1)
         fi fi
    };
};

class Div inherits Factorial {
    div(n: Int, o: Int) : Int {
        n/p
    };
};

class SumSub inherits Div {

    sum(n: Int, o: Int) : Int {
        n + o 
    };
    sub(n: Int, o: Int) : Int {
        n - o
    };
};

class Calculator inherits SumSub {
    mul(n: Int, o: Int) : Int {
        n*o
    };
};

class Main inherits IO {
    a : Results;
    calc: Calculator;
    m : Int;

    main() : SELF_TYPE {
        {
            m <- v;
            a.set_res(calc.mul(5,4));
            out_int(a.get_ress());
            a.set_res(calc@SumSub.sum(5,6));
            out_int(a.get_ress());
            a.set_res(calc@SumSub.sub(5, calc@SumSub.sum(5,6)));
            out_int(a.get_ress());
            a.set_res(calc@Factorial.factorial(5));
            out_int(a.get_ress());
            self;
        }
    } ;

};
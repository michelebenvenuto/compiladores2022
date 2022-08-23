class A {
    a: Int;

    set_var(num : Int) : SELF_TYPE {
      {
         a <- num;
         self;
      }
    };
};

class B inherits A {
    b: Int;
};

class C inherits B {
    c: Int;
};

class D {
    d: Int;

    set_var(num : Int) : SELF_TYPE {
      {
         d <- num;
         self;
      }
    };
    get_d() : Int {
      {
         d;
      }
    };
};

class Main {
    a : Int <- 1;
    b : Int <- 2;
    c : Int;
    d : Int;

    main() : SELF_TYPE {
        {
            (new D).set_var(d);
            self;
        }
    } ;

};
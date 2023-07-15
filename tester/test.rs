fn main() {
    mut S: [usize; n],
    mut X: [usize; q]

    S.sort();

    let len = S.len();
    let mut count = Ok(10);
    let mut t_count = 0;
    for i in X{

        count = S.binary_search(&i);
        if count.is_ok(){
            t_count = count.unwrap();
        }else{
            t_count = count.unwrap_err();
        }

    println!("{:?}",t_count);
    }
}

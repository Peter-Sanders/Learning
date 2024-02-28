use std::fs::File;
use std::io::{self, BufRead};
use::std::path::Path;

fn main() {
    let filename="../advent-storage/advent-23-1.txt";
    let mut result: i32 = 0;
    if let Ok(lines) = read_lines(filename) {
        for line in lines.flatten() {
            // println!("{}", line);
            // let length: i32 = line.chars().count();
            let mut _numdigits = 0;
            let mut digits = String::new();

            for c in line.chars() {
                if c.is_digit(10) {
                    digits.push(c);
                    _numdigits += 1;
                    // println!("{}", c);
                }
            }
            let digi_vec: Vec<char> = digits.chars().collect();
            let mut cal: String = digi_vec[0].to_string().to_owned();
            let last: &str = &digi_vec[_numdigits - 1].to_string();
            cal.push_str(last);
            let cal_int: i32 = cal.parse().unwrap();
            result += cal_int;            
        }
    }
    println!("{}", result);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

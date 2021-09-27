// 枚举引擎改进
mod utils;
use utils::{
    refresh_matrix, enum_comb, refresh_matrixs, cal_table_minenum_recursion, combine
};



fn main() {
    let game_board = vec![
        vec![2,10,3,10,3,10,3,10,3,10,3,10,3,10,3,10,3,10,3,10,1],
        vec![10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        vec![3,10,4,10,4,10,10,10,10,10,10,10,10,10, 10,10,10,10,10,10,10],
        vec![10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        vec![10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        vec![10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        vec![10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        vec![10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        vec![10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        vec![10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    ];

    let (matrix_a, matrix_x, matrix_b) = refresh_matrix(&game_board);
    let (matrix_a_s, matrix_x_s, combination_relationship) = combine(matrix_a, matrix_x);
    let table = cal_table_minenum_recursion(&matrix_a_s, &matrix_x_s, &matrix_b, &combination_relationship);

    // let a: u128 = 0b1111011010110;
    // println!("{:?}", matrix_a.len());

}
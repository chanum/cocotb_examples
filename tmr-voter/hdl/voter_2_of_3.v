
`timescale 1ns/1ps

`default_nettype none

module voter_2_of_3 (
  input clock,

  input reset_in,

  input a_in,
  input b_in,
  input c_in,

  output v_out,
  output v_error_out
);

  reg a_r;
  reg b_r;
  reg c_r;
  reg voter_r;
  reg voter_error_r;

  wire nand1; 
  wire nand2; 
  wire nand3; 

  // Register inputs
  always@(posedge clock) begin
    if (reset_in) begin
      a_r <= 1'b0;
      b_r <= 1'b0; 
      c_r <= 1'b0; 
    end else begin
      a_r <= a_in;
      b_r <= b_in; 
      c_r <= c_in; 
    end
  end

  // Error generator
  always@(a_r, b_r, c_r) begin
    if (a_r == b_r && b_r == c_r) begin
      voter_error_r = 1'b0;
    end else begin
      voter_error_r = 1'b1;
    end
  end

  assign v_error_out = voter_error_r;

  // Voter 2 of 3
  assign nand1 = ~(a_r & b_r);
  assign nand2 = ~(b_r & c_r);
  assign nand3 = ~(a_r & c_r);

  assign v_out = ~(nand1 & nand2 & nand3);

endmodule
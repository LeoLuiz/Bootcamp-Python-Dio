#!/usr/bin/env python3
# -*- coding: utf-8 -*-

menu = """
Bem vindo!

|d| Depositar
|s| Sacar
|e| Extrato
|q| Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
   op = input(menu)
   if op == "d":
      valor = float(input("Qual o valor a ser depositado?\n=>"))
      if(valor > 0):
         saldo += valor
         extrato += f"Deposito: R$ {valor:.2f}\n"
         print("Deposito efetuado com sucesso!")
      else:
         print("Valor inválido!")
   elif op == "s":
      valor = float(input("Qual o valor a ser sacado?\n=>"))
      excedeu_saldo = saldo < valor
      excedeu_saques = LIMITE_SAQUES <= numero_saques
      excedeu_limite = valor > limite
      if(excedeu_saldo):
         print("Erro! Saldo insuficiente!")
      elif(excedeu_saques):
         print("Erro! Limite de saques diários excedido!")
      elif(excedeu_limite):
         print("Erro! O valor excedeu o limite de saque!")
      else:
         saldo -= valor
         numero_saques+=1
         extrato += f"Saque: R$ {valor:.2f}\n"
         print("Saque efetuado com sucesso!")
   elif op == "e":
      print("Extrato")
      print(extrato)
      print("Saldo Atual: R$",saldo)
   elif op == "q":
      break
   else:
      print("opção invalida, por favor selecione novamente a opção desejada.")

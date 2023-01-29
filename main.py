import secrets
import sys
from datetime import datetime
from layout import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import webbrowser



class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_imprimir.clicked.connect(self.gerarpedido)
        self.btn_cancelar.clicked.connect(self.cancelar)

    def gerarpedido(self):
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
        file_id = secrets.token_hex(3)
        self.c = canvas.Canvas(f'Pedido_{file_id}.pdf')

        quantidade = int(self.line_qnt.text())
        unidade = int(self.line_unidade.text())
        entrega = int(self.line_entrega.text())
        quantidade_e_unidade = quantidade * unidade
        valor_final = quantidade_e_unidade + entrega

        if self.line_qnt_2.text().strip() == "":
            pass
        elif self.line_unidade_2.text().strip() == "":
            pass
        elif self.line_entrega2.text().strip() == "":
            pass

        if self.line_qnt_2.text().strip() != "":
            quantidade1 = int(self.line_qnt_2.text())
        else:
            quantidade1 = 0

        if self.line_unidade_2.text().strip() != "":
            unidade1 = int(self.line_unidade_2.text())
        else:
            unidade1 = 0

        if self.line_entrega2.text().strip() != "":
           entrega1 = int(self.line_entrega2.text())
        else:
            entrega1 = 0

        quantidade_e_unidade1 = quantidade1 * unidade1
        valor_final1 = quantidade_e_unidade1 + entrega1

        if valor_final1 != "" and valor_final != "":
            valor = int(valor_final) + int(valor_final1)
        else:
            valor = int(valor_final)

        self.nome = self.input_name.text()
        self.telefone = self.input_telefone.text()
        self.endereco = self.input_endereco.text()

        self.quantidade = self.line_qnt.text()
        self.descricao = self.line_descricao.text()
        self.unidade = self.line_unidade.text()
        self.entrega = self.line_entrega.text()

        self.quantidade1 = self.line_qnt_2.text()
        self.descricao1 = self.line_descricao_2.text()
        self.unidade1 = self.line_unidade_2.text()
        self.entrega1 = self.line_entrega2.text()

        self.c.setFont("Helvetica-Bold", 20)
        self.c.drawString(75, 785, "Recarga de Cartuchos")

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(68, 760, "         Inffo Informática    ")

        self.c.setFont("Helvetica-Bold", 17)
        self.c.drawString(65, 740, "Rua: Quintino Bocaiúva, 160")
        self.c.drawString(68, 720,"CNPJ: 09.004.238/0001-60")


        self.c.setFont("Helvetica-Bold", 14)
        self.c.drawString(50, 680,"Data: ")       
        self.c.drawString(50, 660,"Pedido: ")
        self.c.drawString(50, 640,"Nome: ")
        self.c.drawString(50, 620,"Telefone: ")
        self.c.drawString(50, 600,"Endereco: ")

        self.c.setFont("Helvetica-Bold", 14)
        self.c.drawString(50, 580,"Qnt")
        self.c.drawString(90, 580,"Descricao")
        self.c.drawString(210, 580,"Valor")
        self.c.drawString(260, 580,"Entrega")
        self.c.drawString(200, 510,"Valor Total:")

        self.c.setFont("Helvetica", 12)
        self.c.drawString(60, 565, str(self.quantidade))
        self.c.drawString(80, 565, self.line_descricao.text())
        self.c.drawString(220, 565, str(self.unidade))
        self.c.drawString(280, 565, str(self.entrega))

        self.c.setFont("Helvetica", 12)
        self.c.drawString(60, 550, str(self.quantidade1))
        self.c.drawString(80, 550, str(self.descricao1))
        self.c.drawString(220, 550, str(self.unidade1))
        self.c.drawString(280, 550, str(self.entrega1))

        self.c.setFont("Helvetica",12)
        self.c.drawString(90, 680, data_e_hora_em_texto)
        self.c.drawString(110, 660, file_id)
        self.c.drawString(100, 640, self.input_name.text())
        self.c.drawString(120, 620, self.input_telefone.text())
        self.c.drawString(128, 600, self.input_endereco.text())
        self.c.drawString(280, 510, str(valor))
        self.c.drawString(90, 480, "____________________________")
        self.c.drawString(150, 465, "Assinatura")


        self.c.rect(40, 700, 260, 2, fill=True, stroke=False)
        self.c.rect(40, 530, 260, 2, fill=True, stroke=False)

        self.c.showPage()
        self.c.save()

        self.input_name.setText('')
        self.input_telefone.setText('')
        self.input_endereco.setText('')
        self.line_descricao.setText('')
        self.line_qnt.setText('')
        self.line_entrega.setText('')
        self.line_unidade.setText('')
        self.line_descricao_2.setText('')
        self.line_qnt_2.setText('')
        self.line_entrega2.setText('')
        self.line_unidade_2.setText('')
        webbrowser.open(f"pedido_{file_id}.pdf")

    def cancelar(self):
        self.close()   
   
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
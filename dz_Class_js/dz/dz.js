
class Foto{
    constructor(img,text){
        this.img = img;
        this.text = text
    }  
    fer(){
        document.write("<div class = 't1'>")
        document.write("<div class = 'dv'><img src = "+this.img+" class = 'png'></div>")
        document.write("<div class = 'text'>"+this.text+"</div>")
        document.write("</div>")
    }
}

let foto1 = new Foto("1.png","Работа 24 часа в сутки, 7 дней в неделю, 365 дней в году")
let foto2 = new Foto("2.png","Нет географических границ")
let foto3 = new Foto("3.png","Асортимент")
let foto4 = new Foto("4.png","Безопастность")
let foto5 = new Foto("5.png","Сокращение расходов на аренду и персонал")
let foto6 = new Foto("6.png","Партнерские отнашения")
let foto7 = new Foto("7.png","Покупатель всегда на связи")
let foto8 = new Foto("8.png","Комфортный выбор")
let foto9 = new Foto("9.png","Удобство оплаты")

document.write("<div id='map'>")
document.write("<div  id='pam'>")
foto1.fer();
foto2.fer();
foto3.fer();
foto4.fer();
foto5.fer();
foto6.fer();
foto7.fer();
foto8.fer();
foto9.fer();
document.write("</div>")
document.write("</div>")

































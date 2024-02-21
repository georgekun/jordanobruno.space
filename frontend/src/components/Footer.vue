<template>
    <div class="footer">
       <div class="footer-box">
            <ul>
                <li id="gmail">jorj.knyazyan.15@gmail.com</li>
                <li id="tg">@GeorgiKin</li>
            </ul>
       </div>

       <div class="footer-box">
            <span>Last update: 20.20.2024 15:20 (GMT+3)</span>
       </div>
    </div>
</template>

<script>
export default{
    name: "Footer"
}

</script>

<style scoped>
.footer{
    margin-top:auto;
    display:flex;
    justify-content: space-between;
    color:var(--main-grey);
    flex-wrap:wrap;
    padding-top: 20px;
    padding-bottom:10px;
}

.footer-box:last-child{
    margin-top: auto;
    padding:10px 0;
}
#gmail, #tg {
    position: relative;
    padding-left: 25px; 
  }

#gmail:before, #tg:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 16px; /* Ширина картинки */
    height: 16px; /* Высота картинки */
    background-size: contain;
    background-repeat: no-repeat;
  }
#gmail:before{
    background-image: url("@/assets/gmail.png"); /* Путь к вашей картинке */
}
#tg:before{
    background-image: url("@/assets/telegram.png"); 
}
</style>

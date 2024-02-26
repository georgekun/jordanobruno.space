<template>
    <div class="footer">
       <div class="footer-box" v-if = "getInfoProfile">
            <ul>
                <li id="gmail">gmail: {{getInfoProfile.email}}</li>
                <li id="tg"> telegram: {{getInfoProfile.telegram_link}}</li>
            </ul>
       </div>

       <div class="footer-box">
            <span>Last update: 20.20.2024 15:20 (GMT+3)</span>
       </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default{
    name: "Footer",
    computed:{
        ...mapGetters('main', ['getInfoProfile'])
    }
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

</style>

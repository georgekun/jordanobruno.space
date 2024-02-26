<template>
    <div class="home">
        
        <div class="head">
                <!-- <HomeAvatar></HomeAvatar> -->
                <!-- <h1>Добро пожаловать в мир веб-технологий.
                    <br>
                    Вместе мы превратим Вашу идею в код и создадим уникальное приложение.
                </h1> -->
            <HomeAvatar></HomeAvatar>
            <div>
                <div class="head__text">
                    Погоняло: full stack 
                    <br>
                    Особые приметы: любит копаца в чужом коде
                </div>
                <MainButton 
                    :action="scrollToBottom" 
                    text="написать"/>
            </div>

            
        </div>
        <h2>Изучите недавние работы</h2>
        <ProjectsBoard :latest="true"/>
        <h2>Или напишите сейчас</h2>
        <Form />
    </div>
</template>

<script>
import ProjectsBoard from "@/layouts/ProjectsBoard.vue"
import MainButton from "@/components/MainButton.vue";
import Form from "@/components/Form.vue";
import HomeAvatar from "@/components/HomeAvatar.vue";


export default{
    components:{
    ProjectsBoard,
    MainButton,
    Form,
    HomeAvatar
},
    compuded:{},
    methods:{
        // method for get latest three works
       scrollToBottom(){
            window.scrollTo({
                    top:document.documentElement.scrollHeight,
                    behavior: 'smooth'
                });
       }
    },
    mounted(){}
}
</script>

<style scoped>
.home{
    margin:40px auto;
}

.head{
    width: 100%;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    margin:100px 0;

}
</style>

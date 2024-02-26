<template>
    <div class="home">
        <div class="head_text">
            <div>
                <h1>Добро пожаловать в мир веб-технологий.
                    <br>
                    Вместе мы превратим Вашу идею в код и создадим уникальное приложение.
                </h1>
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

export default{
    components:{
        ProjectsBoard,
        MainButton,
        Form
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
h1{
    text-align: center;
}
</style>

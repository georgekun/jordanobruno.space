<template>
    <div class="custom_form">
        <form @submit.prevent="SEND_APPLICATION_TO_API">
            <label for="name" class="lbl">Как Вас зовут?</label>
            <input 
                id="name"
                type="text" 
                class="fields" 
                placeholder="Введите имя"
                required
                v-model="data.sender_name"
                >

            <label for="contact" class="lbl">Как связаться с Вами?</label>
            <input 
                id="contact"
                type="text" 
                class="fields" 
                placeholder="Введите email или telegram"
                required
                v-model="data.sender_contact"
                >

            <label for="comment" class="lbl">Оставьте комментарий</label>
            <textarea name=""
                id="comment"
                cols="30" 
                rows="5" 
                class="fields" 
                placeholder="Введите комментарий"
                required
                v-model="data.sender_comment"
                ></textarea>

            <div class="btn_cont">
                <button type="submit" :disabled="loading">
                    <MainButton text="Отправить" />
                </button>
            </div>

        </form>
    </div>
</template>

<script>
import axios from "axios"

import MainButton from './MainButton.vue';
import { BASE_URL }  from "@/config";
import { createNewFormData } from "@/utils"
import { mapMutations } from 'vuex'

export default{
    name:"Form",
    components:{
        MainButton
    },
    data(){
        return{
            data:{},
            loading:false
        }
    },
    methods:{
        ...mapMutations('main', ['setMsgStatus']),

        SEND_APPLICATION_TO_API(){
            this.loading = true
            const url = BASE_URL + "form/application/new/"
            let formData = createNewFormData(this.data, [])
            axios.post(url, formData)
                .then( (r) => {this.setMsgStatus(r.data.msg), this.loading=false})
                .catch( () => this.loading = false)
                
        }
    }
}
</script>

<style scoped>
.custom_form{
    max-width: 500px;
    width: 90%;
    margin: 50px auto;
}

.lbl{
    letter-spacing: 1px;
    text-transform: uppercase;
    color:white;
    font-size: 12px;
    font-weight: 300;
    margin:4px 0;
}

.fields{
    width: 100%;
    min-height: 50px;
    color: #fff;
    background-color: #4b4b4b;
    border-style: none;
    border-radius: 3px;
    margin-top: 5px;
    margin-bottom: 19px;
    padding:12px;
    transition: box-shadow .2s;
    border: 2px solid transparent;
}

.fields:focus {
    outline: none; 
    border-color: var(--main-green); 
    transition: 0.6s;
}

.fields:active {
    border-color: var(--main-green); 
    transition: 0.6s;
}
.btn_cont{
    text-align: center;
}
</style>
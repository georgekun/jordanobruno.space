<template>
    <div class="contacts">

        <div class="head_text">
            <div>
                <h1>Давайте начнём что-нибудь вместе!</h1>
            </div>
        </div>
        <div style="display: flex;justify-content: center;">
            <SocialMedia/>
        </div>
        
        <Form />
    </div>
</template>

<script>
import Form from '@/components/Form.vue';
import SocialMedia from '@/components/SocialMedia.vue';

export default{
   components:{
        Form,
        SocialMedia
   }
}
</script>

<style scoped>

.head_text h1{
    font-size:4em
}
.head_text{
    margin-top:12vh;
    min-height: 30vh;
}

@media screen and (max-width:500px){
    .head_text h1{
        font-size:2.3em
    } 
}
</style>
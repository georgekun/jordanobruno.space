<template>
    <div class="contacts">

        <div class="head_text">
            <div>
                <h1>Давайте начнём, что нибудь вместе!</h1>
            </div>
        </div>
        <Form />
    </div>
</template>

<script>
import Form from '@/components/Form.vue';
export default{
   components:{
        Form
   }
}
</script>

<style scoped>

.head_text h1{
    font-size:3em
}
.head_text{
    margin-top:12vh;
    min-height: 30vh;
}
</style>
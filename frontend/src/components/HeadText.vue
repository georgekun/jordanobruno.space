<template>

    <div class="head_info">
        <h6 class="subtitle">привет, я</h6>  
        <h6 class="title">Князян Джордж</h6>
        <p>Web-разработчик</p>
    </div>

</template>

<script>



export default{
    name:"HeadText",
    components:{
    }   
}
</script>

<style scoped>

.head_info{
    color:rgba(255, 255, 255, 0.691);
    margin-top:50px;
    margin-bottom:80px;
}
.subtitle{
    margin-bottom: 0;
    font-size: 25px;
    font-weight: 500;
}

.title{
    padding:0;
    margin-bottom: 0px;
    font-size: 65px;
    font-weight: bold;
}
.head_info p{
    margin-top: -5px;
    font-size: 22px;
}
</style>
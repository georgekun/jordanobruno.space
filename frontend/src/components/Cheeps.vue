<template>
    <div class="cheeps">
        <!-- <h3>Стек: </h3> -->
        <div>
            <span
                class="cheeps_item"
                v-for="cheep in names" 
                :key="cheep.id"
            >
                {{ cheep }}
            </span>
        </div>
    </div>
</template>

<script>
export default{
    name:"Cheeps",
    props:{
        names: Array,
    }
}
</script>

<style scoped>
h3{
    text-align: left;
    margin:auto 10px auto 5px;
}
.cheeps{
    margin:30px 0;
}
.cheeps > div{
    display: flex;
    justify-content: center;
    grid-gap:5px;
    width: 100%;
    max-width: 500px;
    flex-wrap: wrap;
    margin:auto;
    color:black;
    font-weight: 500;
  
}
.cheeps_item{
    background-color: var(--main-grey);
    width: auto;
    max-height: 50px;
    padding:5px 10px;
    border-radius: 10px;
    text-align: center;
}
</style>
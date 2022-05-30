<template>
  <div class="home">
    <div class="container">
      <div class="texto">
        <h3> Relação de Operadoras Ativas ANS</h3>
        <input type="file" id="upload-csv" accept=".csv" ref='file' v-on:change="handleFileUpload()"/>
        <button id="upload" v-on:click="submitFile()"> Save </button>
        <input type="text" ref="filtro" v-model="message" />
        <button v-on:click="filtrar()"> Filter </button>
      </div>
      <div class="arquivos">
          
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: 'Container'
    }
</script>

<style>
.home {
    margin-top: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .container{
    width: 95%; 
    background: #fff;
    border-radius: 4px;
    padding: 12px;
  }
  .container .texto {
    display: flex;
    justify-content: space-between;
  }
  .container h3 {
    color: #5161f1;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 20px;
    line-height: 23px;
  }
  /* ==================================== DATAGRID ============================== */
  .arquivos{
    padding: 1rem;
    overflow-x:scroll;
    text-align: center;
  }
</style>
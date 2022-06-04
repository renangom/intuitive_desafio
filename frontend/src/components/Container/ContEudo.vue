<template>
  <div class="home">
    <div class="container">
      <div class="texto">
        <h3> Relação de Operadoras Ativas ANS</h3>
        <input type="file" id="upload-csv" accept=".csv" ref='file' @change="handleFileUpload()"/>
        <button id="upload" v-on:click="submitFile()" class="btn btn-sm btn-success"> Save </button>
        <input type="text" ref="filtro" />
        <button v-on:click="filtrar()" class="btn btn-success"> Filter </button>
      </div>
      <div class="botoes">
        <button v-on:click="add" class="btn btn-primary "> Adicionar Operadora </button>
        <button v-on:click="ocultar" class="btn btn-dark "> Ocultar </button>
      </div>
      <!-- =========================================== FORMULÁRIO ====================================-->
      <!-- ===========================================================================================-->
      <div class="arquivos">
        <div class="" v-if="seen">
          <input type="hidden" v-model="url" class="form-control mt-2" placeholder="url"  />
          <input type="number" class="form-control mt-2" placeholder="RegistroANS" v-model="RegistroANS" />
          <input type="number" class="form-control mt-2" placeholder="CNPJ" v-model="CNPJ" />
          <input type="text" class="form-control mt-2" placeholder="RazaoSocial" v-model="RazaoSocial" />
          <input type="text" class="form-control mt-2" placeholder="NomeFantasia" v-model="NomeFantasia" />
          <input type="text" class="form-control mt-2" placeholder="Modalidade" v-model="Modalidade" />
          <input type="text" class="form-control mt-2" placeholder="Logradouro" v-model="Logradouro" />
          <input type="text" class="form-control mt-2" placeholder="Numero" v-model="Numero" />
          <input type="text" class="form-control mt-2" placeholder="Complemento" v-model="Complemento" />
          <input type="text" class="form-control mt-2" placeholder="Bairro" v-model="Bairro" />
          <input type="text" class="form-control mt-2" placeholder="Cidade" v-model="Cidade" />
          <input type="text" class="form-control mt-2" placeholder="UF" v-model="UF" />
          <input type="number" class="form-control mt-2" placeholder="CEP" v-model="CEP" />
          <input type="number" class="form-control mt-2" placeholder="DDD" v-model="DDD" />
          <input type="number" class="form-control mt-2" placeholder="Telefone" v-model="Telefone" />
          <input type="number" class="form-control mt-2" placeholder="Fax" v-model="Fax" />
          <input type="text" class="form-control mt-2" placeholder="Endereco" v-model="Endereco" />
          <input type="text" class="form-control mt-2" placeholder="Representante" v-model="Representante" />
          <input type="text" class="form-control mt-2" placeholder="CargoRepresentante" v-model="CargoRepresentante" />
          <input type="date" class="form-control mt-2" placeholder="DataRegistroANS" v-model="DataRegistroANS" />
          <button v-on:click="postCSV()" class="btn btn-block btn-success"> Salvar </button>
        </div>
        <!-- =========================================== TABELA ====================================-->
        <!-- ===========================================================================================-->
        <div class="adicionar">
          <table class="table">
              <thead>
                <th>RegistroANS</th>
                <th>CNPJ</th>
                <th>RazaoSocial</th>
                <th>NomeFantasia</th>
                <th>Modalidade</th>
                <th>Logradouro</th>
                <th>Numero</th>
                <th>Complemento</th>
                <th>Bairro</th>
                <th>Cidade</th>
                <th>UF</th>
                <th>CEP</th>
                <th>DDD</th>
                <th>Telefone</th>
                <th>Fax</th>
                <th>Endereco</th>
                <th>Representante</th>
                <th>CargoRepresentante</th>
                <th>DataRegistroANS</th>
              </thead>
              <tbody>
                <tr v-for="dado in csv" v-bind:key="dado.url">
                    <td>{{dado.RegistroANS}}</td>
                    <td>{{dado.CNPJ}}</td>
                    <td>{{dado.NomeFantasia}}</td>
                    <td>{{dado.RazaoSocial}}</td>
                    <td>{{dado.Modalidade}}</td>
                    <td>{{dado.Logradouro}}</td>
                    <td>{{dado.Numero}}</td>
                    <td>{{dado.Complemento}}</td>
                    <td>{{dado.Bairro}}</td>
                    <td>{{dado.Cidade}}</td>
                    <td>{{dado.UF}}</td>
                    <td>{{dado.CEP}}</td>
                    <td>{{dado.DDD}}</td>
                    <td>{{dado.Telefone}}</td>
                    <td>{{dado.Fax}}</td>
                    <td>{{dado.Endereco}}</td>
                    <td>{{dado.Representante}}</td>
                    <td>{{dado.CargoRepresentante}}</td>
                    <td>{{dado.DataRegistroANS}}</td>
                    <td>
                        <button @click="getOne(dado)" class="btn btn-sm btn-success"><i class="fa fa-pencil"></i></button>
                    </td>
                    <td>
                        <button @click="deleteOne(dado.url)" class="btn btn-sm btn-danger"><i class="fa fa-trash"></i></button>
                    </td>
                </tr>
                <tr v-for="dado in content.data" v-bind:key="dado.url">
                    <td>{{dado.RegistroANS}}</td>
                    <td>{{dado.CNPJ}}</td>
                    <td>{{dado.NomeFantasia}}</td>
                    <td>{{dado.RazaoSocial}}</td>
                    <td>{{dado.Modalidade}}</td>
                    <td>{{dado.Logradouro}}</td>
                    <td>{{dado.Numero}}</td>
                    <td>{{dado.Complemento}}</td>
                    <td>{{dado.Bairro}}</td>
                    <td>{{dado.Cidade}}</td>
                    <td>{{dado.UF}}</td>
                    <td>{{dado.CEP}}</td>
                    <td>{{dado.DDD}}</td>
                    <td>{{dado.Telefone}}</td>
                    <td>{{dado.Fax}}</td>
                    <td>{{dado.Endereco}}</td>
                    <td>{{dado.Representante}}</td>
                    <td>{{dado.CargoRepresentante}}</td>
                    <td>{{dado.DataRegistroANS}}</td>
                </tr>
              </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    import axios from 'axios'
    import Papa from 'papaparse'
    export default {
        name: 'ContEudo',
        mounted(){
            this.getAll()
        },
        /* ====================================== DEFININDO DADOS =================================== */
        /* ====================================================================================== */
        data() {
            return{
                seen: false,
                csv : null,
                url: '',
                RegistroANS: 0,
                CNPJ: 0,
                RazaoSocial : '',
                NomeFantasia: '',
                Modalidade: '',
                Logradouro: '',
                Numero: '',
                Complemento: '',
                Bairro: '',
                Cidade: '',
                UF: '',
                CEP: 0,
                DDD: 0,
                Telefone: 0,
                Fax: 0,
                Endereco: '',
                Representante: '',
                CargoRepresentante: '',
                DataRegistroANS: '',
                file: '',
                content: [],
                parsed: false,
                obj: null

            }
        },
        methods: {

          /* ====================================== MÉTODO GET =================================== */
          /* ====================================================================================== */
            getAll(){
                axios.get('http://127.0.0.1:8000/SCV/')
                .then((res) => {
                    this.csv = res.data 
                    this.url = '';
                    this.RegistroANS = 0
                    this.CNPJ = 0
                    this.RazaoSocial = ''
                    this.NomeFantasia = ''
                    this.Modalidade = ''
                    this.Logradouro  = ''
                    this.Numero = ''
                    this.Complemento = ''
                    this.Bairro = ''
                    this.Cidade = ''
                    this.UF = ''
                    this.CEP = 0
                    this.DDD = 0
                    this.Telefone = 0
                    this.Fax = ''
                    this.Endereco = ''
                    this.Representante = ''
                    this.CargoRepresentante = ''
                    this.DataRegistroANS = 0
                })
            },
            /* ====================================== MÉTODO QUE RETORNAR DADO =================================== */
            /* ====================================================================================== */
            getOne(dado){
              this.url = dado.url;
              this.RegistroANS = dado.RegistroANS
              this.CNPJ = dado.CNPJ
              this.RazaoSocial = dado.RazaoSocial
              this.NomeFantasia = dado.NomeFantasia
              this.Modalidade = dado.Modalidade
              this.Logradouro  = dado.Logradouro
              this.Numero = dado.Numero
              this.Complemento = dado.Complemento
              this.Bairro = dado.Bairro
              this.Cidade = dado.Cidade
              this.UF = dado.UF
              this.CEP = dado.CEP
              this.DDD = dado.DDD
              this.Telefone = dado.Telefone
              this.Fax = dado.Fax
              this.Endereco = dado.Endereco
              this.Representante = dado.Representante
              this.CargoRepresentante = dado.CargoRepresentante
              this.DataRegistroANS = dado.RegistroANS
            },
            /* ====================================== MÉTODO DELETE =================================== */
            /* ====================================================================================== */
            deleteOne(url){
              axios.delete(url, {auth:{
                username : 'renan',
                password : '123'
              }})
              .then(() =>{
                this.getAll()
              })
            },
            /* ====================================== MÉTODO POST =================================== */
            /* ====================================================================================== */
            postCSV(){
              if(this.url == ''){
                 axios.post(`http://127.0.0.1:8000/SCV/`,
                {RegistroANS: this.RegistroANS, CNPJ: this.CNPJ, RazaoSocial: this.RazaoSocial,
                NomeFantasia: this.NomeFantasia, Modalidade: this.Modalidade, Logradouro: this.Logradouro,
                Numero: this.Numero, Complemento: this.Complemento, Bairro: this.Bairro, Cidade: this.Cidade,
                UF: this.UF, CEP: this.CEP, DDD: this.DDD, Telefone: this.Telefone, Fax: this.Fax,
                Endereco: this.Endereco, Representante: this.Representante, CargoRepresentante: this.CargoRepresentante,
                DataRegistroANS: this.DataRegistroANS},
                {auth:{username: 'renan', password: '123'}},
                )
                .then(() => {
                  this.getAll()
                  })
                .catch(() => {
                    alert('Campo UF deve conter apenas 2 caracteres')
                })
                }else{
                   axios.put(this.url,
                  {RegistroANS: this.RegistroANS, CNPJ: this.CNPJ, RazaoSocial: this.RazaoSocial,
                  NomeFantasia: this.NomeFantasia, Modalidade: this.Modalidade, Logradouro: this.Logradouro,
                  Numero: this.Numero, Complemento: this.Complemento, Bairro: this.Bairro, Cidade: this.Cidade,
                  UF: this.UF, CEP: this.CEP, DDD: this.DDD, Telefone: this.Telefone, Fax: this.Fax,
                  Endereco: this.Endereco, Representante: this.Representante, CargoRepresentante: this.CargoRepresentante,
                  DataRegistroANS: this.DataRegistroANS},
                  {auth:{username: 'renan', password: '123'}},
                  )
                  .then(() => {
                    this.getAll()
                  })
                  .catch(() => {
                    alert('Campo UF deve conter apenas 2 caracteres')
                  })
                }
            },
            /* ======================================FUNÇÕES DO FORMULÁRIO ADICIONAR =================================== */
            /* ====================================================================================== */
            add(){
              this.seen = true
            },
            ocultar(){
              this.seen = false
            },

            /* ====================================== FUNÇÃO FILTRO DADOS=================================== */
            /* ====================================================================================== */
            filtrar(){

            },
            /* ====================================== SUBMETER CSV =================================== */
            /* ====================================================================================== */
            submitFile(){
              console.log(this.content.data)
              axios.post('http://127.0.0.1:8000/SCV/', this.content.data,{auth:{username: 'renan', password: '123'}}
              ).then(function(){
                console.log("DEU GREEN")
              }).catch(function(){
                console.log("Não deu green")
              })
            },
            /* ======================================FUNÇÃO QUE INTERPRETA O CSV=================================== */
            /* ====================================================================================== */
            handleFileUpload(){
              this.file = this.$refs.file.files[0]
              this.parseFile()
            },
            parseFile(){
              Papa.parse(this.file, {
                header: true,
                skipEmptyLines: true,
                complete: function(results){
                  this.content = results
                  this.parsed = true
                }.bind(this)
              })
              this.obj = Object.assign({}, this.csv, this.content)
            }
        }
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
    overflow-y: scroll;
    text-align: center;
  }

  .botoes button{
    margin-right: 1rem;
  }
</style>
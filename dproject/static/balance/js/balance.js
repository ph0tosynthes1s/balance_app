new Vue({
    el:'#balance__table',
    data:{
        balances:[],
        user_balance: ''
    },
    delimiters: ['[[',']]'],
    created:
    function () {
        const vm = this;
        axios.get('/api/balances')
        .then(function (response){
            vm.balances = response.data
        })
    },
    methods:{
        addSubmit(){
            const vm = this;
            const user = document.querySelector('#balance__add_user-id').value
            const sum = document.querySelector('#balance__add_sum').value
            const newAdd = {'user': user, 'add': sum}
            axios.post('api/balances/', newAdd)
            .then(function (response){
                vm.balances = response.data
            })
            axios.get('/api/balances')
            .then(function (response){
                vm.balances = response.data
            })
        },
        removeSubmit(){
            const vm = this;
            const user = document.querySelector('#balance__remove_user-id').value
            const sum = document.querySelector('#balance__remove_sum').value
            const newRemove = {'user': user, 'remove': sum}
            axios.post('api/balances/', newRemove)
            .then(function (response){
                vm.balances = response.data
            })
            axios.get('/api/balances')
            .then(function (response){
                vm.balances = response.data
            })
        },
        exchangeSubmit(){
            const vm = this;
            const root = document.querySelector('#balance__exchange_root').value
            const endpoint = document.querySelector('#balance__exchange_endpoint').value
            const sum = document.querySelector('#balance__exchange_sum').value
            const newExchange = {'root': root, 'endpoint': endpoint, 'exchange': sum}
            axios.post('api/balances/', newExchange)
            .then(function (response){
                vm.balances = response.data
            })
            axios.get('/api/balances')
            .then(function (response){
                vm.balances = response.data
            })
        },
        getBalanceSubmit(){
            const vm = this;
            const userBalanceId = document.querySelector('#balance__get_balance-id').value
            const newBalance = {'user': userBalanceId, 'balance': 1}
            axios.post('api/balances/', newBalance)
            .then(function (response){
                data = response.data[0]
                user_id = data.id
                balance = data.balance
                vm.user_balance = `Id: ${user_id} Баланс: ${balance}`
            })
            .catch(function(response){
                vm.user_balance = `Вы ввели неправильный ID`
            })
        },
    },
})
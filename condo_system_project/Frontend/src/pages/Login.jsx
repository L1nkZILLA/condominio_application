import React, {useState} from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function Login(){
  const [company, setCompany] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const nav = useNavigate();

  async function handleSubmit(e){
    e.preventDefault();
    try{
      const form = new URLSearchParams();
      form.append('username', email);
      form.append('password', password);
      const res = await axios.post('http://localhost:8001/auth/login', form);
      localStorage.setItem('token', res.data.access_token);
      nav('/admin');
    }catch(err){
      alert('Erro no login');
    }
  }

  return (
    <div style={{maxWidth:400, margin:'auto', padding:20}}>
      <h2>Login - Condomínio</h2>
      <form onSubmit={handleSubmit}>
        <input placeholder='Empresa' value={company} onChange={e=>setCompany(e.target.value)} style={{width:'100%', marginBottom:8}}/>
        <input placeholder='Email' value={email} onChange={e=>setEmail(e.target.value)} style={{width:'100%', marginBottom:8}}/>
        <input placeholder='Senha' type='password' value={password} onChange={e=>setPassword(e.target.value)} style={{width:'100%', marginBottom:8}}/>
        <button type='submit'>Entrar</button>
      </form>
    </div>
  );
}

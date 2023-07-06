import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"
import { useState } from "react";
import axios from 'axios'

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export const signUp = async(email:string, password:string) => {
    console.log(email)
    console.log(password)
    let response = await axios.post('signup/', {
        'email':email,
        'password':password
    });
    console.log(response);    
}

export default function SignUp() {

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [buttonClicked, setButtonClicked] = useState(false);

    const handleSubmit = (e:any) => {
        e.preventDefault()
        setButtonClicked(true)
        signUp(email, password)
        setEmail("")
        setPassword("")
      };


    return(
        <Form onSubmit={handleSubmit}>

            <Form.Group className="mb-3" controlId="signUpEmail" onChange={(e) => setEmail(e.target.value)}>
                <Form.Label>Email Address</Form.Label>
                <Form.Control type="email" placeholder="unique@emailaddr.ess" value={email} />
            </Form.Group>

            <Form.Group className="mb-3" controlId="signUpPassword" onChange={(e) => setPassword(e.target.value)}>
                <Form.Label>Password</Form.Label>
                <Form.Control type="password" placeholder="Password (8-40 characters)" value={password}/>
                <Form.Text className="text-muted">Enter a password between 8-40 characters</Form.Text>
            </Form.Group>

            <Button variant="primary" type="submit">Sign Up</Button>
            {buttonClicked && <p style={{ marginTop: '10px', fontStyle: 'italic', color: 'green', fontSize: '10px' }}> Welcome to BeerBuddies! Please log in to continue.</p>}
        </Form>
    );

}
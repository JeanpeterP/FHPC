import React from 'react'
import Icon1 from '../../images/welcome_cats.svg'
import Icon2 from '../../images/welcome_cats.svg'
import Icon3 from '../../images/welcome_cats.svg'

import { ServicesCard, ServicesContainer, ServicesH1, ServicesH2, ServicesIcon, ServicesP, ServicesWrapper } from './ServicesElements'

const Services = () => {
  return (
    <ServicesContainer id="services">
        <ServicesH1>Our Services</ServicesH1>
        <ServicesWrapper>
            <ServicesCard>
                <ServicesIcon src={Icon1}/>
                <ServicesH2>Drop ins</ServicesH2>
                <ServicesP>We help care for your pet when you are not around</ServicesP>
            </ServicesCard>
            <ServicesCard>
                <ServicesIcon src={Icon2}/>
                <ServicesH2>Overnight Stays</ServicesH2>
                <ServicesP>We help care for your pet when you are not around</ServicesP>
            </ServicesCard>
            <ServicesCard>
                <ServicesIcon src={Icon3}/>
                <ServicesH2>Extended stay care</ServicesH2>
                <ServicesP>We help care for your pet when you need to leave for weeks at a time</ServicesP>
            </ServicesCard>
        </ServicesWrapper>
    </ServicesContainer>
  )
}

export default Services
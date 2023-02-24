import React, {useState} from 'react'
import Video from '../../videos/HeroVideo.mp4'
import {Button} from '../ButtonElement'
import {
    HeroContainer,
    HeroContent,
    HeroH1,
    HeroP,
    HeroBtnWrapper,
    ArrowForward,
    ArrowRight,
    HeroBg,
    VideoBg
} from './HeroElements';

const HeroSection = () => {
    const [hover, setHover] = useState(false)

    const onHover = () => {
        setHover(!hover)
    }

  return (
    <>
        <HeroContainer id="home">
            <HeroBg>
                <VideoBg autoPlay loop muted src={Video} type='video/mp4' />
            </HeroBg>
            <HeroContent>
                <HeroH1>Quality Pet Care for all!</HeroH1>
                <HeroP>
                    Sign up today and receive 50% off your first service appointment with us!
                </HeroP>
                <HeroBtnWrapper>
                    <Button to="signup" onMouseEnter={onHover} onMouseLeave={onHover}
                    primary='true'
                    dark='true'
                    >
                        Register your pet today! {hover ? <ArrowForward /> : <ArrowRight />}
                    </Button>
                </HeroBtnWrapper>
            </HeroContent>
        </HeroContainer>
    </>
  )
}

export default HeroSection
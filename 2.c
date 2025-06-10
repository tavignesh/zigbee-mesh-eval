#include "samd20_sysctrl.h"
#include "gclk.h"
static void gclk_init(void);
static void gclk_config_main_clk(int clk_src);

int main(void) {

		uint64_t devid = 0x0a;
		uint64_t sbit = 0xff;
		uint64_t ebit = 0xfe;
		uint64_t dta = 0xf4f4f4f4f4f4f4f4;
		uint64_t pktid = 0x000000;
	
		uint64_t frame1 = 0x7E001C1001000000; //7E 00 1C 10 01 00 00 00       
		uint64_t frame2 = 0x0000000000fffe00; //00 00 00 00 00 FF FE 00 
		uint64_t frame3 = 0x0000000000000000; //00 FF 01 01 00 00 F4 F4 
		uint64_t frame4 = 0x0000000000000000; //F4 F4 F4 F4 F4 F4 FE 52
	
		uint64_t devid64 = devid << 40;
		uint64_t sbit64 = sbit << 48;
		uint64_t ebit64 = ebit << 8;
		uint64_t pktid64 = pktid << 16;
		frame3 = frame3 + devid64 + sbit64 + pktid64 + ((dta & 0xffff000000000000) >> 48);
		frame4 = frame4 + ebit64 + ((dta & 0x0000ffffffffffff) << 16);
		
		//devid64 = 0x0000ff0000000000	f3
		//pktid64 = 0x000000ffffff0000	f3
		//sbit64 =  0x00ff000000000000	f3
		//ebit64 =  0x000000000000ff00	f4
		//dta64 =   0xffffffffffff0000	f4 000000000000ffff  f3
		//csum64 =  0x00000000000000ff	f4
		
	  gclk_init();
    gclk_config_main_clk(GCLK_GENCTRL_SRC_OSC8M_Val);
		PORT->Group[1].DIRSET.reg = 0x1000;
		//PORT->Group[1].OUTSET.reg = 0X1000;

    PM->APBCMASK.reg |= (1U << 2);// PM
	  while(GCLK->STATUS.bit.SYNCBUSY){};
			
    *((int *)0x42000800U) |= 0x1;// SERCOM0 SWRST 
    while((*((int *)0x42000800U) & 1)){
      /* The module is busy resetting itself */
    }
    while((*((int *)0x42000800U) & 2)){
             /* enable */
     }
    while(GCLK->STATUS.reg & GCLK_STATUS_SYNCBUSY){};         

   
    GCLK->CLKCTRL.reg = 0x400D;
                
    while(GCLK->STATUS.bit.SYNCBUSY & GCLK_STATUS_SYNCBUSY){};
		PORT->Group[0].PINCFG[4].bit.PMUXEN = 1;
		PORT->Group[0].PINCFG[5].reg = 0x3;
		PORT->Group[0].PMUX[2].reg = 0x33;            // PORT
    
                        
    while(SERCOM0->USART.STATUS.bit.SYNCBUSY | GCLK->STATUS.bit.SYNCBUSY){}; 	
		SERCOM0->USART.CTRLA.reg = 0x40100004;					// SERCOM0 CTRLA
    while(SERCOM0->USART.STATUS.bit.SYNCBUSY  | GCLK->STATUS.bit.SYNCBUSY){}; 
    SERCOM0->USART.BAUD.reg = 65536 * (1 - (16 * 9600.0 / 1000000.0));
    SERCOM0->USART.CTRLB.reg = 0x30000; 						//  CTRLB
    while(SERCOM0->USART.STATUS.bit.SYNCBUSY | GCLK->STATUS.bit.SYNCBUSY){}; 	
    SERCOM0->USART.CTRLA.reg |= 0x2;					// SERCOM0 CTRLA
    while(SERCOM0->USART.STATUS.bit.SYNCBUSY | GCLK->STATUS.bit.SYNCBUSY){};
		
		uint64_t pktid8 = 0x00;
		while (1) {
				//if(SERCOM0->USART.INTFLAG.bit.RXS){
				//		PORT->Group[1].OUTSET.reg = 0X1000;
				//		while(!SERCOM0->USART.INTFLAG.bit.RXC){};
				//		while(SERCOM0->USART.STATUS.bit.SYNCBUSY | GCLK->STATUS.bit.SYNCBUSY){}; // SYNCBUSY
				//		dd = SERCOM0->USART.DATA.reg;
				//		while(SERCOM0->USART.STATUS.bit.SYNCBUSY | GCLK->STATUS.bit.SYNCBUSY){}; // SYNCBUSY
						//PORT->Group[1].OUTCLR.reg = 0X1000;
				//}
			
				if(pktid == 0x0 & pktid8 < 0xffffff){
							pktid8 = pktid8 + 0x1;
							frame3 = frame3 & 0xffffff000000ffff;
							frame3 = frame3 + (pktid8 << 16);
				}
				
				uint64_t csum = 0x0;
				uint64_t g = frame3 & 0x00ffffffffffffff;
				frame4 = frame4 & 0xffffffffffffff00;
				for(int i=0;i<8;i++){
							csum = (csum + (g & 0xff)) & 0xff;
							g = g >> 8;
				}
				g = frame4 & 0xffffffffffffff00;
				for(int i=0;i<8;i++){
							csum = (csum + (g & 0xff)) & 0xff;
							g = g >> 8;
				}
				
				g = frame2;
				for(int i=0;i<8;i++){
							csum = (csum + (g & 0xff)) & 0xff;
							g = g >> 8;
				}
				
				g = frame1 & 0x000000ffffffffff;
				for(int i=0;i<8;i++){
							csum = (csum + (g & 0xff)) & 0xff;
							g = g >> 8;
				}
				
				csum = (0xff - csum) & 0xff;
				frame4 = frame4 + csum;
				
				PORT->Group[1].OUTTGL.reg = 0X1000;
				
				//printf("%"PRIx64 "\n", csum);
				
				uint64_t h = 0x0;
				uint64_t j = frame1;
				for(int i = 0;i<8;i++){
							h = (j & 0xff00000000000000) >> 56;
							j = j << 8;
							SERCOM0->USART.DATA.reg = h;
							while(!SERCOM0->USART.INTFLAG.bit.TXC){};
				}
				
				j = frame2;
				for(int i = 0;i<8;i++){
							h = (j & 0xff00000000000000) >> 56;
							j = j << 8;
							SERCOM0->USART.DATA.reg = h;
							while(!SERCOM0->USART.INTFLAG.bit.TXC){};
				}
				
				j = frame3;
				for(int i = 0;i<8;i++){
							h = (j & 0xff00000000000000) >> 56;
							j = j << 8;
							SERCOM0->USART.DATA.reg = h;
							while(!SERCOM0->USART.INTFLAG.bit.TXC){};
				}
				
				j = frame4;
				for(int i = 0;i<8;i++){
							h = (j & 0xff00000000000000) >> 56;
							j = j << 8;
							SERCOM0->USART.DATA.reg = h;
							while(!SERCOM0->USART.INTFLAG.bit.TXC){};
				}
				
				for(int i = 99999;i!=0;i--){
				int wkejnweijvn = 100;
				}
				
				while(SERCOM0->USART.STATUS.bit.SYNCBUSY | GCLK->STATUS.bit.SYNCBUSY){};		// SYNCBUSY
    }
	}

static void gclk_init(void) {
 /* Enable the APB_APBA clock - where the GCLK uses this clock */
    PM->APBAMASK.reg |= PM_APBAMASK_GCLK;
 
 /* Software reset the module to ensure it is re-initialized correctly */
    GCLK->CTRL.reg = GCLK_CTRL_SWRST;
 
    while(GCLK->CTRL.reg & GCLK_CTRL_SWRST){
	 /* wait for reset to complete */
    }
}


static void gclk_config_main_clk(int clk_src) {
 while((GCLK->STATUS.reg & GCLK_STATUS_SYNCBUSY));
// 
 /* Write the Divisor value to the register */
 GCLK->GENDIV.reg  = GCLK_GENDIV_DIV(0);
// *((uint8_t*)&GCLK->GENDIV.reg) = GCLK_GENDIV_DIV(0);// |GCLK_GENDIV_ID(gclk_id);
 
 /* Wait for synchronization */
 while((GCLK->STATUS.reg & GCLK_STATUS_SYNCBUSY));
 GCLK->GENCTRL.reg = (GCLK->GENCTRL.reg & GCLK_GENCTRL_GENEN) | \
					  GCLK_GENCTRL_ID(0) | GCLK_GENCTRL_RUNSTDBY | \
					  GCLK_GENCTRL_SRC(clk_src);
	
 /* Wait for synchronization */
 while((GCLK->STATUS.reg & GCLK_STATUS_SYNCBUSY));
}


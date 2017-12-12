///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Nov 23 2017)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

BaseMainWind::BaseMainWind( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText1 = new wxStaticText( this, wxID_ANY, wxT("lable1"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText1->Wrap( -1 );
	bSizer1->Add( m_staticText1, 0, wxALL, 5 );
	
	m_textCtrl1 = new wxTextCtrl( this, wxID_ANY, wxT("t3st"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer1->Add( m_textCtrl1, 0, wxALL, 5 );
	
	button_main = new wxButton( this, wxID_ANY, wxT("anniu"), wxDefaultPosition, wxDefaultSize, wxBU_BOTTOM );
	bSizer1->Add( button_main, 0, wxALL, 5 );
	
	
	this->SetSizer( bSizer1 );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	button_main->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( BaseMainWind::main_button_click ), NULL, this );
}

BaseMainWind::~BaseMainWind()
{
	// Disconnect Events
	button_main->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( BaseMainWind::main_button_click ), NULL, this );
	
}
